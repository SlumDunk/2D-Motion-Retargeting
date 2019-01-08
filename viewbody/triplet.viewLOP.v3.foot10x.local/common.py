import torch
import os
import json
import utils


class Config:
    #device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    proj_dir = '/data1/wurundi/fbxMotionDisentangled/'
    exp_name = os.getcwd().split('/')[-1]
    exp_dir = os.path.join(proj_dir, exp_name)
    log_dir = os.path.join(exp_dir, 'log/')
    model_dir = os.path.join(exp_dir, 'model/')
    stat_path = os.path.join(proj_dir, 'statistic-view.csv')

    img_size = (512, 512)
    unit = 256
    len_frames = 64
    len_joints = 28

    foot_weight = 10
    triplet_margin = 1
    triplet_weight = 0.1

    mot_en_channels = [len_joints, 64, 96, 128]
    body_en_channels = [len_joints, 64, 96, 128]
    de_channels = [mot_en_channels[-1] + body_en_channels[-1], 128, 64, len_joints]

    nr_epochs = 500
    batch_size = 64
    lr = 1e-3

    save_frequency = 50
    val_frequency = 50
    visualize_frequency = 1000

    utils.ensure_dirs([proj_dir, log_dir, exp_dir, model_dir])


config = Config()