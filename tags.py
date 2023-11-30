from aws_cdk import Stack, Tags


def tag_stacks(stacks: list, env_name: str, project_name: str):
    for stack in stacks:
        Tags.of(stack).add("Environment", env_name)
        Tags.of(stack).add("Project", project_name)
