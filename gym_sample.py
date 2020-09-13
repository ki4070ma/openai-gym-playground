#!/usr/bin/env python

import gym


def chk_env():
    envids = [spec.id for spec in gym.envs.registry.all()]
    print(envids)


if __name__ == "__main__":
    chk_env()
    env = gym.make("MountainCar-v0")
    observation = env.reset()
    env.render()
    for _ in range(2000):
        env.render()
        env.step(env.action_space.sample())
