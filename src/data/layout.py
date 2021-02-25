# -*- encoding: utf-8 -*-
"""Layout dataset
"""
import os
from .loadresponse import LoadResponse, mat_loader


class LayoutDataset(LoadResponse):
    """Layout dataset (mutiple files) generated by 'layout-generator'.
    """

    def __init__(
        self,
        root,
        sub_dir,
        list_path=None,
        train=True,
        transform=None,
        target_transform=None,
        load_name="F",
        resp_name="u",
    ):
        subdir = os.path.join("train", "train") \
            if train else os.path.join("test", "test")

        # find the path of the list of train/test samples
        list_path = os.path.join(root, sub_dir, list_path)

        # find the root path of the samples
        root = os.path.join(root, sub_dir, subdir)

        super().__init__(
            root,
            mat_loader,
            list_path,
            load_name=load_name,
            resp_name=resp_name,
            extensions="mat",
            transform=transform,
            target_transform=target_transform,
        )
