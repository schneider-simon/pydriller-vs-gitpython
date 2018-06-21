from pydriller import RepositoryMining


def pydriller_task1(path):
    java_commits = []
    commit_counter = 0
    mine = RepositoryMining(path)
    # How can I get the total amount of commits before traverse?
    for commit in mine.traverse_commits():
        commit_counter += 1
        java_paths = [m.filename for m in commit.modifications if m.filename.endswith('java')]

        print("%s" % commit_counter)

        if len(java_paths) > 0:
            java_commits.append(commit)

    print("Total commits: %s, Commits touching Java: %s" % (commit_counter, len(java_commits)))
    # Total commits: 4005, Commits touching Java: 2631

    return java_commits


def pydriller_task2(path):
    mine = RepositoryMining(path)
    file_sizes = {}

    commit_counter = 0
    for commit in mine.traverse_commits():
        commit_counter += 1

        print("%s" % commit_counter)

        for modification in commit.modifications:
            path = modification.new_path
            if path not in file_sizes:
                file_sizes[path] = []

            current_size = file_sizes[path][-1] if len(file_sizes[path]) > 0 else 0
            next_size = current_size + modification.added - modification.removed
            file_sizes[path].append(next_size)

    return file_sizes
