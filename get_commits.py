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


def save_commits_to_file(commits, filename):
    with open(filename, 'w') as file:
        json.dump(commits, file, indent=4)


def main():
    username = 'ArashGorji'
    repo = 'MaktabsharifMiniProject3'
    token = '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'

    commits = get_commits(username, repo, token=token)
    save_commits_to_file(commits, 'commits.json')


if __name__ == "__main__":
    main()
