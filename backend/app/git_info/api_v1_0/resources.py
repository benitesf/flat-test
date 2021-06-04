import json
from flask import request, Blueprint
from flask_restful import Api, Resource

from github import Github

git_info_v1_0_bp = Blueprint('git_info_v1_0_bp', __name__)

api = Api(git_info_v1_0_bp)

repo_name = "benitesf/fullstack-interview-test"
g = Github("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")

class BranchListResource(Resource):
    def get(self):
        repo = g.get_repo(repo_name)
        res = {"branches": []}
        for b in repo.get_branches():
            res["branches"].append({"name": b.name})
        return json.dumps(res)


class BranchDetailResource(Resource):
    def get(self, branch_name):
        res = {"commits": [], "status": "200", "message": ""}        
        try:
            repo = g.get_repo(repo_name)    
            for c in repo.get_commits():
                com = {}
                com["sha"] = c.sha
                com["author"] = c.author.name
                com["date"] = c.committer.created_at
                mess = []
                for com in c.get_comments():
                    mess.append({"message": com.body})
                com["comments"] = mess
                res.append(com)
        except:
            res["status"] = "404"
            res["message"] = "Branch Not Found"

        return json.dumps(res)

class CommitDetaillResource(Resource):
    def get(self, commit_code):
        #return commit
        pass

api.add_resource(BranchListResource, '/api/v1.0/branchs', endpoint='branch_list_resource')
api.add_resource(BranchDetailResource, '/api/v1.0/branchs/<string:branch_name>', endpoint='branch_detail_resource')
api.add_resource(CommitDetaillResource, '/api/v1.0/commits/<string:commit_code>', endpoint='commit_detail_resource')

#api.add_resource(PullRequestCreateResource, '')
#api.add_resource(PullRequestViewResource, '')