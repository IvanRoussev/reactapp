import subprocess
import argparse


def automate_build(image_name, dockerfile_path):
    try:
        subprocess.run(
            ["docker", "build", "-t", image_name, dockerfile_path], check=True
        )
        print("Created Image: ", image_name)

    except subprocess.CalledProcessError as e:
        print("Error: Couldn't Build image:", e)
        raise


def run_container(image_name, name_container):
    try:
        subprocess.run(
            [
                "docker",
                "run",
                "--name",
                name_container,
                "-d",
                "-p",
                "3000:3000",
                image_name,
            ]
        )

    except subprocess.CalledProcessError as e:
        print("Error: Couldn't spin up docker container:", e)
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Automate build and run for a Dockerized React app."
    )
    parser.add_argument("image_name", type=str, help="Name for the Docker image")
    parser.add_argument("dockerfile_path", type=str, help="Path to the Dockerfile")
    parser.add_argument(
        "name_container", type=str, help="Name for the Docker container"
    )
    parser.add_argument(
        "--rebuild", action="store_true", help="Rebuild the Docker image"
    )

    args = parser.parse_args()

    if args.rebuild:
        print("Building Image and running container")
        automate_build(args.image_name, args.dockerfile_path)
        run_container(args.image_name, args.name_container)
    else:
        print("Running container")
        run_container(args.image_name, args.name_container)


if __name__ == "__main__":
    main()
