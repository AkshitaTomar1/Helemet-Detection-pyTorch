from helmet.configuration.s3_operations import S3Operation
from helmet.entity.config_entity import ModelPusherConfig
from helmet.components.model_pusher import ModelPusher

if __name__ == "__main__":
    config = ModelPusherConfig()
    s3_op = S3Operation()
    pusher = ModelPusher(config, s3_op)

    artifact = pusher.initiate_model_pusher()
    print("✅ Model pushed to:", artifact.s3_model_path)
