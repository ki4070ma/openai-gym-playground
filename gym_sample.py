#!/usr/bin/env python

import gym


def chk_env():
    envids = [spec.id for spec in gym.envs.registry.all()]
    print(envids)


if __name__ == "__main__":
    # chk_env()
    env = gym.make("MountainCar-v0")
    observation = env.reset()
    print(observation)
    print(env.observation_space.high)
    print(env.observation_space.low)
    env.render()
    for _ in range(2000):
        env.render()
        print(env.step(env.action_space.sample()))
