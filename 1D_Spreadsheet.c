// STATEMENT: https://www.codingame.com/training/easy/1d-spreadsheet

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

struct cell {
        char *operation;
        int val_1;
        int val_2;
        struct cell *dep_1;
        struct cell *dep_2;
        int calculated; // 1 if calculated, else 0
        int value;
    };

int eval(struct cell *cell) {
    if(cell->calculated)
        return cell->value;
    else {
        if(cell->dep_1 != NULL) 
            cell->val_1 = eval(cell->dep_1);
        if(cell->dep_2 != NULL)
            cell->val_2 = eval(cell->dep_2);
        
        cell->value = calculate(cell->operation, cell->val_1, cell->val_2);
        cell->calculated = 1;
        return cell->value;
    }
}

int calculate(char *operation, int val_1, int val_2) {
    if(strcmp(operation, "VALUE") == 0)
        return val_1;
    else if(strcmp(operation, "ADD") == 0)
        return val_1 + val_2;
    else if(strcmp(operation, "SUB") == 0)
        return val_1 - val_2;
    else if(strcmp(operation, "MULT") == 0)
        return val_1 * val_2;
}

int main()
{
    int N;
    scanf("%d", &N);

    struct cell *dependency_graph = (struct cell*)malloc(N * sizeof(struct cell));

    for (int i = 0; i < N; i++) {
        char operation[6];
        char arg_1[7];
        char arg_2[7];
        scanf("%s%s%s", operation, arg_1, arg_2);

        dependency_graph[i].operation = (char *)malloc(6*sizeof(char));
        strcpy(dependency_graph[i].operation, operation);
        if(arg_1[0] == '$') {
            int dep_addr = atoi(arg_1+1);
            dependency_graph[i].dep_1 = &dependency_graph[dep_addr];
        }
        else {
            dependency_graph[i].val_1 = atoi(arg_1);
            dependency_graph[i].dep_1 = NULL;
        }

        if(arg_2[0] == '$') {
            int dep_addr = atoi(arg_2+1);
            dependency_graph[i].dep_2 = &dependency_graph[dep_addr];
        }
        else if(arg_2[0] != '_') {
            dependency_graph[i].val_2 = atoi(arg_2);
            dependency_graph[i].dep_2 = NULL;
        }

        // Straight calculation. Base cases for eval recursion
        if(dependency_graph[i].dep_1 == NULL && dependency_graph[i].dep_2 == NULL) {
            dependency_graph[i].value = calculate(dependency_graph[i].operation, dependency_graph[i].val_1, dependency_graph[i].val_2);
            dependency_graph[i].calculated = 1;
        }
    }
    int curr_cell;
    for (int i = 0; i < N; i++) {
        curr_cell = eval(&dependency_graph[i]);
        printf("%d\n", curr_cell);
    }

    return 0;
}