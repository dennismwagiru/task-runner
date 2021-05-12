db.createUser(
    {
        user: "flaskuser",
        pwd: "1234",
        roles: [
            {
                role: "readWrite",
                db: "taskrunner"
            }
        ]
    }
)

db.createCollection('tasks')