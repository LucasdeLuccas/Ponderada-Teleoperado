from setuptools import setup

package_name = 'Ponderada_Teleoperado'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lucas de Luccas',
    maintainer_email='lucas.luccas@sou.inteli.edu.br',
    description='Projeto de interação com Turtlebot usando ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'user_interface = Ponderada_Teleoperado.user_interface:main',
            'robo_teleop = Ponderada_Teleoperado.robo_teleop:main',
        ],
    },
)
