import os
import environs

try:
    env = environs.Env()
    env.read_env("./.env")
except FileNotFoundError:
    print("No .env file found, using os.environ.")

api_id = 21705136
api_hash = "78730e89d196e160b0f1992018c6cb19"

STRINGSESSION = os.getenv("S", env.str("S"))

second_session = os.getenv("SECOND_SESSION", env.str("SECOND_SESSION", ""))

db_type = "mongodb"
db_url = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
db_name = "toxic"

apiflash_key = "76b05dd14bf148f49e1dadc98b5f61cf"
rmbg_key = os.getenv("RMBG_KEY", env.str("RMBG_KEY", ""))
vt_key = "26809ec198954a226106354659c8da99c68148c6883f60f2c457b33cfe3b217d"
gemini_key = os.getenv("GEMINI_KEY", env.str("GEMINI_KEY", ""))
cohere_key = os.getenv("KEY")

pm_limit = int(os.getenv("PM_LIMIT", env.int("PM_LIMIT", 4)))

test_server = bool(os.getenv("TEST_SERVER", env.bool("TEST_SERVER", False)))
modules_repo_branch = os.getenv(
    "MODULES_REPO_BRANCH", env.str("MODULES_REPO_BRANCH", "master")
)
