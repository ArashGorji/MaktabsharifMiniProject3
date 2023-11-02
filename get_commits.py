import requests
import json


def get_commits(username, repo, token=None):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    headers = {"Authorization": f"Bearer {token}"}
    if token:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)
    commits = response.json()
    return commits


def sort_commits_by_author(commits):
    commits.sort(key=lambda commit: commit['commit']['author']['name'])
    return commits


def save_commits_to_file(commits, filename):
    with open(filename, 'w') as file:
        json.dump(commits, file, indent=4)


def main():
    username = 'ArashGorji'
    repo = 'MaktabsharifMiniProject3'
    token = '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'

    commits = get_commits(username, repo, token=token)
    sorted_commits = sort_commits_by_author(commits)
    save_commits_to_file(sorted_commits, 'commits_sorted.json')


if __name__ == "__main__":
    main()
