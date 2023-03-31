from quart import Quart, jsonify
import sample_service.respository.organization_repository as organization_repository

app = Quart(__name__)


@app.route("/api/v1/organizations", methods=['GET'])
async def get_organizations():
    response = jsonify(organization_repository.get_organizations())
    return response


if __name__ == "__main__":
    print(app.url_map)
    app.run()
