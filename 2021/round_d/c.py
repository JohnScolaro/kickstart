def solve() -> str:
    num_problem_sets, num_students = [int(e) for e in input().split()]
    problem_sets = []
    for _ in range(num_problem_sets):
        i = input().split()
        problem_sets.append((int(i[0]), int(i[1])))
    student_skills_to_be_tested = [int(x) for x in input().split()]

    answer = []

    for student_skill in student_skills_to_be_tested:
        answer.append(get_problem_set_for_student(problem_sets, student_skill))

    return ' '.join(str(x) for x in answer)

def get_problem_set_for_student(problem_sets, student_skill):
    index = get_index_of_problem_set_to_use(problem_sets, student_skill)
    problem_difficulty = get_difficulty_to_use(problem_sets, index, student_skill)
    mutate_problem_sets_for_efficiency(problem_sets, index, student_skill)
    return problem_difficulty

def get_index_of_problem_set_to_use(problem_sets, student_skill):
    minimum = 10E19
    indexs_of_min = []
    for i, b in enumerate(problem_sets):
        d = diff(b[0], b[1], student_skill)
        if d == 0:
            return i
        if d < minimum:
            minimum = d
            indexs_of_min = [i]
        if d == minimum:
            indexs_of_min.append(i)
    for i in indexs_of_min:
        if problem_sets[i][1] < student_skill:
            return i
    return indexs_of_min[0]

def get_difficulty_to_use(problem_sets, index, student_difficulty_level):
    problem_set_to_use = problem_sets[index]
    if student_difficulty_level < problem_set_to_use[0]:
        return problem_set_to_use[0]
    if student_difficulty_level > problem_set_to_use[1]:
        return problem_set_to_use[1]
    return student_difficulty_level

def mutate_problem_sets_for_efficiency(problem_sets, index, student_difficulty_level):
    # pop the index no matter what
    problem_set_to_mutate = problem_sets.pop(index)
    
    if problem_set_to_mutate[0] == problem_set_to_mutate[1]:
        return
    elif student_difficulty_level < problem_set_to_mutate[0]: # Lower
        problem_sets.append((problem_set_to_mutate[0] + 1, problem_set_to_mutate[1]))
    elif student_difficulty_level > problem_set_to_mutate[1]: # Higher
        problem_sets.append((problem_set_to_mutate[0], problem_set_to_mutate[1] - 1))
    elif (student_difficulty_level > problem_set_to_mutate[0]) and (student_difficulty_level < problem_set_to_mutate[1]): # Inside
        problem_sets.append((problem_set_to_mutate[0], student_difficulty_level - 1))
        problem_sets.append((student_difficulty_level + 1, problem_set_to_mutate[1]))
    elif student_difficulty_level == problem_set_to_mutate[0]: # Lower edge
        problem_sets.append((problem_set_to_mutate[0] + 1, problem_set_to_mutate[1]))
    elif student_difficulty_level == problem_set_to_mutate[1]: # Upper edge
        problem_sets.append((problem_set_to_mutate[0], problem_set_to_mutate[1] - 1))
    return

def diff(range_a, range_b, difficulty):
    if difficulty < range_a:
        return range_a - difficulty
    if difficulty > range_b:
        return difficulty - range_b
    return 0

T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))

