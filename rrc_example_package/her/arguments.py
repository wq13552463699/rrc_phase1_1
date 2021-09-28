import argparse

"""
Here are the param for the training

"""

def get_args():
    parser = argparse.ArgumentParser()
    
    # DDPG + HER og args
    parser.add_argument('--n-epochs', type=int, default=300, help='the number of epochs to train the agent')
    parser.add_argument('--n-cycles', type=int, default=50, help='the times to collect samples per epoch')
    parser.add_argument('--n-batches', type=int, default=40, help='the times to update the network')
    parser.add_argument('--save-interval', type=int, default=5, help='the interval that save the trajectory')
    parser.add_argument('--seed', type=int, default=123, help='random seed')
    parser.add_argument('--num-workers', type=int, default=1, help='the number of cpus to collect samples')
    parser.add_argument('--replay-strategy', type=str, default='future', help='the HER strategy')
    parser.add_argument('--clip-return', type=float, default=50, help='if clip the returns')
    parser.add_argument('--save-dir', type=str, default='rrc_example_package/her/saved_models/', help='the path to save the models')
    parser.add_argument('--noise-eps', type=float, default=0.2, help='noise eps')
    parser.add_argument('--random-eps', type=float, default=0.3, help='random eps')
    parser.add_argument('--buffer-size', type=int, default=int(1e6), help='the size of the buffer')
    parser.add_argument('--replay-k', type=int, default=4, help='ratio to be replace')
    parser.add_argument('--clip-obs', type=float, default=200, help='the clip ratio')
    parser.add_argument('--batch-size', type=int, default=256, help='the sample batch size')
    parser.add_argument('--gamma', type=float, default=0.98, help='the discount factor')
    parser.add_argument('--action-l2', type=float, default=1, help='l2 reg')
    parser.add_argument('--lr-actor', type=float, default=0.001, help='the learning rate of the actor')
    parser.add_argument('--lr-critic', type=float, default=0.001, help='the learning rate of the critic')
    parser.add_argument('--polyak', type=float, default=0.95, help='the average coefficient')
    parser.add_argument('--n-test-rollouts', type=int, default=10, help='the number of tests')
    parser.add_argument('--clip-range', type=float, default=5, help='the clip range')
    parser.add_argument('--demo-length', type=int, default=20, help='the demo length')
    parser.add_argument('--cuda', action='store_true', help='if use gpu do the acceleration')
    parser.add_argument('--num-rollouts-per-mpi', type=int, default=2, help='the rollouts per mpi')
    
    # New RRC specific args
    parser.add_argument('--noisy-resets', type=int, default=0, help='whether to perturb default reset positions')
    parser.add_argument('--noise-level', type=int, default=1, help='magnitude of noise for resets')
    parser.add_argument('--exp-dir', type=str, default='exp', help='experiment folder name')
    parser.add_argument('--z-reward', type=int, default=1, help='whether to include cube height based reward')
    parser.add_argument('--ep-len', type=int, default=90, help='Length of episode')
    parser.add_argument('--xy-only', type=int, default=1, help='Only use xy positions for sparse reward calculation')
    parser.add_argument('--steps-per-goal', type=int, default=30, help='steps per goal change')
    parser.add_argument('--z-scale', type=float, default=20, help='scale z/height rewards')
    parser.add_argument('--domain-randomization', type=int, default=0, help='whether to use domain randomization')
    parser.add_argument('--step-size', type=int, default=50, help='whether to use domain randomization')
    parser.add_argument('--action-type', type=str, default='torque', help='type of action to use')
    parser.add_argument('--obs-type', type=str, default='default', help='type of obs to use')
    parser.add_argument('--difficulty', type=int, default=3, help='goal difficulty level')
    parser.add_argument('--increase-fps', type=int, default=0, help='whether to increase camera fps')
    parser.add_argument('--trajectory-aware', type=int, default=0, help='whether to make agent aware it is dealing with trajectories')
    parser.add_argument('--disable-arm3', type=int, default=0, help='whether to disable the robots 3rd arm')
    
    args = parser.parse_args()
    return args
