# Ultralytics YOLO 🚀, AGPL-3.0 license

import re
from pathlib import Path
from setuptools import setup

# Settings
FILE = Path(__file__).resolve()
PARENT = FILE.parent # root directory
README = (PARENT / 'README.md').read_text(encoding='utf-8')


def get_version():
    """
    Retrieve the version number from the 'ultralytics/__init__.py' file.

    Returns:
        (str): The version number extracted from the '__version__' attribute in the 'ultralytics/__init__.py' file.
    """
    file = PARENT / 'ultralytics/__init__.py'
    return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(encoding='utf-8'), re.M)[1]


def parse_requirements(file_path: Path):
    """
    Parse a requirements.txt file, ignoring lines that start with '#' and any text after '#'.

    Args:
        file_path (str | Path): Path to the requirements.txt file.

    Returns:
        (List[str]): List of parsed requirements.
    """
    requirements = []
    for line in Path(file_path).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            requirements.append(line.split('#')[0].strip()) # ignore inline comments

    return requirements


setup(
    name='vsensebox-ultralytics', # name of pypi package
    version=get_version(), # version of pypi package
    python_requires='>=3.8',
    license='AGPL-3.0',
    description=('Ultralytics YOLO for SOTA object detection, multi-object tracking, instance segmentation, '
                 'pose estimation and image classification.'),
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/numediart/ultralytics-for-vsensebox',
    project_urls={'Bug Reports': 'https://github.com/numediart/ultralytics-for-vsensebox/issues',
                  'Source': 'https://github.com/numediart/ultralytics-for-vsensebox'},
    packages=['ultralytics'] + [str(x) for x in Path('ultralytics').rglob('*/') if x.is_dir() and '__' not in str(x)],
    package_data={'ultralytics': ['**/*.yaml', '**/*.sh', '../tests/*.py'], 'ultralytics.assets': ['*.jpg'], 'ultralytics.solutions.templates': ['*.html']},
    include_package_data=True,
    install_requires=parse_requirements(PARENT / 'requirements.txt'),
    extras_require={
        'export': [
            "numpy<2.0.0", # TF 2.20 compatibility
            "onnx>=1.12.0; platform_system != 'Darwin'", # ONNX export
            "onnx>=1.12.0,<1.18.0; platform_system == 'Darwin'",  # TF inference hanging on MacOS
            "coremltools>=8.0; platform_system != 'Windows' and python_version <= '3.13'", # CoreML supported on macOS and Linux
            "scikit-learn>=1.3.2; platform_system != 'Windows' and python_version <= '3.13'", # CoreML k-means quantization
            "openvino>=2024.0.0",  # OpenVINO export
            "tensorflow>=2.0.0,<=2.19.0", # TF bug https://github.com/ultralytics/ultralytics/issues/5161
            "tensorflowjs>=2.0.0", # TF.js export, automatically installs tensorflow
            "tensorstore>=0.1.63; platform_machine == 'aarch64' and python_version >= '3.9'", # for TF Raspberry Pi exports
            "h5py!=3.11.0; platform_machine == 'aarch64'", # fix h5py build issues due to missing aarch64 wheels in 3.11 release
        ],
        'extra': [
            "ipython", # interactive notebook
            "albumentations>=1.4.6", # training augmentations
            "faster-coco-eval>=1.6.7", # COCO mAP
        ],
        'solutions': [
            "shapely>=2.0.0", # shapely for point and polygon data matching
            "streamlit>=1.29.0", # for live inference on web browser, i.e `yolo streamlit-predict`
            "flask>=3.0.1", # for similarity search solution
        ],
        'logging': [
            "wandb", # https://docs.ultralytics.com/integrations/weights-biases/
            "tensorboard", # https://docs.ultralytics.com/integrations/tensorboard/
            "mlflow", # https://docs.ultralytics.com/integrations/mlflow/
        ],
        'typing': [
            "scipy-stubs",
            "types-pillow",
            "types-psutil",
            "types-pyyaml",
            "types-requests",
            "types-shapely",
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows', ],
    keywords="machine-learning, deep-learning, computer-vision, ML, DL, AI, YOLO, YOLOv3, YOLOv5, YOLOv8, YOLOv9, YOLOv10, YOLO11, HUB, Ultralytics",
    entry_points={'console_scripts': ['yolo = ultralytics.cfg:entrypoint', 'ultralytics = ultralytics.cfg:entrypoint']}
)
