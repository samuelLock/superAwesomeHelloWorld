Synopsis: Flask webapp that responds with a static 'Hello World" webpage.

How To Use:
    -   Link CircleCI pipeline to repo (https://circleci.com/docs/2.0/getting-started/)
    -   The pipeline requires 3 environment variables to be set manually: (https://circleci.com/docs/2.0/ecs-ecr/)
        . AWS_ACCESS_KEY_ID
        . AWS_SECRET_ACCESS_KEY
        . AWS_DEFAULT_REGION
    -   The pipeline has two workflows:
        . Local build of the flask app and check that "Hello World!" is returned
        . Build the docker image and push it to the ECR repo. (https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)

Limitations:
    -   The pipelines requires the ECS environment to already be set up. (See https://github.com/samuelLock/SAHW-Infrastructure)
    -   The call to ECR to get the RepositoryID expects there to only be one repository. If there are multiple, the image will be pushed to the zero-indexed repository returned using the CLI.