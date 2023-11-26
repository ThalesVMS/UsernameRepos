from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    repositories = response.json()
    return repositories


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        repositories = get_repositories(username)
        repo_names = [repo['name'] for repo in repositories]
        total_repos = len(repo_names)
        return render_template('index.html', repo_names=repo_names, total_repos=total_repos)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
