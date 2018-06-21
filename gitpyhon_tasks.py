from git import Repo


def gitpython_task1(path):
    repo = Repo(path)
    all_commits = list(repo.iter_commits('master'))
    java_commits = []

    i = 0
    for commit in all_commits:
        tree = commit.tree
        # Function in tree that returns all files? blob returns files in root only
        files = tree.blobs

        i += 1

        print("%s / %s" % (i, len(all_commits)))
        # Found out that stats object already holds all touched files later
        java_files = [path for path in commit.stats.files if path.endswith(".java")]

        if len(java_files) > 0:
            java_commits.append(commit)

    print("Commits total: %s, Commits touching Java Files: %s" % (len(all_commits), len(java_commits)))
    # Result: Commits total: 4005, Commits touching Java Files: 2631

    return java_commits


def gitpython_task2(path):
    repo = Repo(path)

    all_commits = list(repo.iter_commits('master'))

    file_sizes = {}

    commit_counter = 0
    for commit in all_commits:
        commit_counter += 1

        print("%s / %s" % (commit_counter, len(all_commits)))
        for path in commit.stats.files:
            stats = commit.stats.files[path]

            if path not in file_sizes:
                file_sizes[path] = []

            # Easier to collect file sizes since lines already includes file size
            # Execution is hower much slower
            file_sizes[path].append(stats["lines"])

    return file_sizes
