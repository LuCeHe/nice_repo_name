import os, time, string, random, shutil

# define the paths
CDIR = os.path.abspath(os.path.dirname(__file__))
WORKDIR = os.path.abspath(os.path.join(CDIR, '..'))
DATADIR = os.path.abspath(os.path.join(WORKDIR, 'data'))
EXPSDIR = os.path.abspath(os.path.join(WORKDIR, 'experiments'))

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%Y-%m-%d--%H-%M-%S--", named_tuple)
characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for i in range(5))
EXPDIR = os.path.join(EXPSDIR, time_string + random_string + '_project_name')
os.makedirs(EXPDIR, exist_ok=True)


def get_args():
    import argparse
    parser = argparse.ArgumentParser(description='LLM Experiment Arguments')
    parser.add_argument(
        '--experiment_name', type=str, default=EXPDIR,
        help='Name of the experiment directory'
    )
    parser.add_argument(
        '--data_dir', type=str, default=DATADIR,
        help='Directory for data'
    )
    parser.add_argument(
        '--work_dir', type=str, default=WORKDIR,
        help='Working directory'
    )
    parser.add_argument(
        '--layers', type=int, default=12,
        help='Number of layers in the model'
    )
    parser.add_argument(
        '--hidden_size', type=int, default=768,
        help='Size of the hidden layers'
    )
    return parser.parse_args()


def main():

    # get the arguments that will be used as your experiment configuration
    args = get_args()

    # here you would typically set up your experiment
    time.sleep(60*30)  # simulate some setup time

    # here we will simply write the arguments to a file
    args_file = os.path.join(args.experiment_name, 'args.txt')
    with open(args_file, 'w') as f:
        for key, value in vars(args).items():
            f.write(f"{key}: {value}\n")

    # and another with lorem ipsum text
    lorem_ipsum_file = os.path.join(args.experiment_name, 'lorem_ipsum.txt')
    with open(lorem_ipsum_file, 'w') as f:
        f.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Sed do eiusmod tempor incididunt ut labore "
            "et dolore magna aliqua."
        )

    # zip the experiment directory
    shutil.make_archive(EXPDIR, 'zip', EXPDIR)
    print('Done')


if __name__ == "__main__":
    main()
