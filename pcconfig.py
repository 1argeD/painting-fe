import pynecone as pc


config = pc.Config(
    app_name="app",
    db_url="sqlite:///pynecone.db",
    port="3000",
    env=pc.Env.DEV,
)
