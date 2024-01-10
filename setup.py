from setuptools import setup, find_packages

setup(
    name='deepeye',       
    # Start with a small number and increase it with every change you make
    version='0.1.0',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Utility tools for image enhancement.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='esunvoteb',                   # Type in your name
    author_email='esun@voteb.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/SyngularXR/DeepEye',
    # download_url='https://github.com/ImagineersHub/compipe/archive/v_01.tar.gz',    # I explain this later on
    keywords=['python', 'blender'],   # Keywords that define your package best
    packages=find_packages(),
    install_requires=[            # I get to this in a second
        "torch==2.0.0+cu117",
        "torchaudio==2.0.1+cu117",
        "torchvision==0.15.1+cu117",
        "numpy==1.24.2",
        "opencv-contrib-python==4.7.0.72"
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.10',
    ],
)