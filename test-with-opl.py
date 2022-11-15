#!/usr/bin/env python3

import argparse
import sys

import opl.args
import opl.locust
import opl.skelet

import testing


def doit(args, status_data):
    test_set = testing.MyAppUser

    status_data.set('name', 'perfscale-demo-app API perf test')

    return opl.locust.run_locust(args, status_data, test_set, new_stats=True)


def main():
    parser = argparse.ArgumentParser(
        description='perfscale-demo-app API perf test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    opl.args.add_locust_opts(parser)
    with opl.skelet.test_setup(parser) as (args, status_data):
        return doit(args, status_data)


if __name__ == "__main__":
    sys.exit(main())
