from src.IoC_OSO.class_models import *

projectList = [
    Project(
        id="P1",
        name="simple Test",
        AAS=[
            BuildingElementAAS(
                id="4b519fc8ccd2482881166aeeb1fa056b",
                type="ifcFooting",
                name="Main Footing",
                parameters=[
                    Weight(value=65, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=25, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=25)
                    ]
                ),
            BuildingElementAAS(
                id="bfba99c57904a3cb8716b21e5506f06",
                type="ifcColumn",
                name="Concrete Column 1",
                parameters=[
                    Weight(value=1.4, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.525, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.525)
                    ]
                ),
            BuildingElementAAS(
                id="a02ce42f83254486aa1edb1247dea7f7",
                type="ifcColumn",
                name="Concrete Column 2",
                parameters=[
                    Weight(value=1.4, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.525, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.525)
                    ]
                ),
            BuildingElementAAS(
                id="01af405746f949f08ad80a771fd86c90",
                type="ifcColumn",
                name="Concrete Column 3",
                parameters=[
                    Weight(value=1.4, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.525, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.525)
                    ]
                ),
            BuildingElementAAS(
                id="27bacd0fd64c44b28f14f46f219ff53f",
                type="ifcColumn",
                name="Concrete Column 4",
                parameters=[
                    Weight(value=1.4, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.525, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.525)
                    ]
                ),
            BuildingElementAAS(
                id="a34b310143484104a2dc19fbf1414f1c",
                type="ifcColumn",
                name="Steel Column 1",
                parameters=[
                    Weight(value=4.1, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.525, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.525)
                    ]
                ),
            BuildingElementAAS(
                id="c62ccbb8934241608073c534d374b29f",
                type="ifcColumn",
                name="Steel Column 2",
                parameters=[
                    Weight(value=4.1, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.525, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.525)
                    ]
                ),
            BuildingElementAAS(
                id="b866c927bf7e4ffd84bbc2cb4d8551c9",
                type="ifcMember",
                name="Concrete Member Short 1",
                parameters=[
                    Weight(value=0.585, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.225, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.225)
                    ]
                ),
            BuildingElementAAS(
                id="d3114c0f446d4346a48ae2a82f552d89",
                type="ifcMember",
                name="Concrete Member Short 2",
                parameters=[
                    Weight(value=0.585, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.225, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.225)
                    ]
                ),
            BuildingElementAAS(
                id="4a33da56c39941d5a8aecde19cb40988",
                type="ifcMember",
                name="Steel Member 1",
                parameters=[
                    Weight(value=1.71, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=1.425, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=1.425)
                ]
            ),
            BuildingElementAAS(
                id="23d54e8f0fad45b180fd306126a25ba5",
                type="ifcMember",
                name="Steel Member 2",
                parameters=[
                    Weight(value=11.1, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=1.425, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=1.425)
                ]
            ),
            BuildingElementAAS(
                id="b515fc6a95fe48b99cd535b9532981b6",
                type="ifcMember",
                name="Wood Member 1",
                parameters=[
                    Weight(value=11.1, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=1.425, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=1.425)
                ]
            ),
            BuildingElementAAS(
                id="d491b69b7ae546208138ee5e65efb940",
                type="ifcBeam",
                name="Steel Beam 1",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="08fc56dcac8a46869d22bf9cd0c5ba7b",
                type="ifcBeam",
                name="Steel Beam 2",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="767f8828012a4f5b9993e2c69790cd62",
                type="ifcBeam",
                name="Steel Beam 3",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="0d6b41dd61e14368b95dba144328f82c",
                type="ifcBeam",
                name="Steel Beam 4",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="8cadacc1886144d69590db328332a2ab",
                type="ifcBeam",
                name="Steel Beam 5",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="27417a4ecaec432eb451a7d74a6d341d",
                type="ifcBeam",
                name="Steel Beam 6",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="f731ddf151034e3e8e3281adada2b1e5",
                type="ifcBeam",
                name="Steel Beam 7",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="b8f68166f28a452785e1d73d10979579",
                type="ifcBeam",
                name="Steel Beam 8",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="1b2a01a770b64c4b93fc54f0b8d97097",
                type="ifcBeam",
                name="Steel Beam 9",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="09b2d01e080042abbaa48c7ec24a0118",
                type="ifcBeam",
                name="Steel Beam 10",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="725cde43ee9a42ae99a3fa6fd5753046",
                type="ifcBeam",
                name="Steel Beam 11",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="812201272c7147d1aabd86555136ce81",
                type="ifcBeam",
                name="Steel Beam 12",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="f956d095f3fb44b19795dd1662a51494",
                type="ifcBeam",
                name="Steel Beam 13",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            ),
            BuildingElementAAS(
                id="1d2ed4f5bd024bb2b4ef1e318e161c91",
                type="ifcBeam",
                name="Steel Beam 14",
                parameters=[
                    Weight(value=6.435, dimensionName="Gewicht", dimensionUnit="t"),
                    Volume(value=0.825, dimensionName="Volumen", dimensionUnit="m^3"),
                    PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t", value=0.825)
                ]
            )
            ],
        ResourceAAS =[
            TransportResourceAAS(
            id="bb69d2fd9629450a9fd700c3c6954381",
            type="Kran",
            name="Crane L1-24",
            setups=[
                Setup(
                    id="s001",
                    type="Transport",
                    name="Schwerlasthaken",
                    capabilities=[
                        TransportCapability(
                            id="c001",
                            name="Transport001",
                            description="Transport schwerer Güter",
                            parameters=[
                                Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[5, 80]),
                                PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t/h", value=2),
                                Velocity(dimensionName="Verfahrgeschwindigkeit", dimensionUnit="km/h", value=2),
                                Height(dimensionName="Verfahrhöhe", dimensionUnit="m", valueRange=[0, 15]),
                                Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 28])
                                ]
                            ),
                        PositioningCapability(
                            id="c002",
                            name="Positionieren",
                            description="Poitionieren schwerer Güter",
                            parameters=[
                                Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 70]),
                                PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t/h", value=2),
                                Velocity(dimensionName="Verfahrgeschwindigkeit", dimensionUnit="km/h", value=2),
                                Height(dimensionName="Verfahrhöhe", dimensionUnit="m", valueRange=[0, 15]),
                                Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 30])
                                ]
                            )
                        ]
                     ),
                Setup(
                    id="s002",
                    type="Transport",
                    name="Haken",
                    capabilities=[
                        TransportCapability(
                            id="c002",
                            name="Transport003",
                            description="Transport leichter Güter",
                            parameters=[
                                Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 25]),
                                Velocity(dimensionName="Verfahrgeschwindigkeit", dimensionUnit="km/h", value=1),
                                PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t/h", value=1),
                                Height(dimensionName="Verfahrhöhe", dimensionUnit="m", valueRange=[0, 2]),
                                Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 10])
                            ]
                        )
                    ]
                )
            ]
        ),
        TransportResourceAAS(
            id="04229d8896464647a7c2c4e11b45ad7f",
            type="Kran",
            name="Robot KR 120 R3900",
            setups=[
                Setup(
                    id="s001",
                    type="Transport",
                    name="Schwerlasthaken",
                    capabilities=[
                        PositioningCapability(
                            id="c002",
                            name="Positionieren",
                            description="Poitionieren schwerer Güter",
                            parameters=[
                                Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 1]),
                                PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t/h", value=2),
                                Velocity(dimensionName="Verfahrgeschwindigkeit", dimensionUnit="km/h", value=2),
                                Height(dimensionName="Verfahrhöhe", dimensionUnit="m", valueRange=[0, 4]),
                                Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 1])
                                ]
                            )
                        ]
                     ),
            ]
        ),
        TransportResourceAAS(
            id="34a375c631364af4bd4e72d5d365d3dc",
            type="LKW",
            name="Truck MAN 20t",
            setups=[
                Setup(
                id="s002",
                type="Transport",
                name="Hänger",
                    capabilities=[
                        TransportCapability(
                        id="c002",
                        name="Transport002",
                        description="Transport leichter Güter",
                        parameters=[
                            Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 15]),
                            Velocity(dimensionName="Verfahrgeschwindigkeit", dimensionUnit="km/h", value=3),
                            PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t/h", value=3),
                            Height(dimensionName="Verfahrhöhe", dimensionUnit="m", valueRange=[0, 15]),
                            Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 10])
                            ]
                        )
                    ]
                )
                ],
            ),
                WorkerResourceAAS(
                    id="1fa7facc81a344078fdb0444102c777e",
                    type="Worker",
                    name="Worker_001",
                    setups=[
                        Setup(
                            id="s003",
                            type="Qualification",
                            name="Schrauben",
                            capabilities=[
                                AdjustCapability(
                                    id="c003",
                                    name="JustierenName",
                                    description="Justieren Beschreibung",
                                    parameters=[
                                        Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 70]),
                                        Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 20]),
                                        PerfVolume(dimensionName="Justagegeschwindigkeit", dimensionUnit="t/h", value=0.5)
                                    ]
                                ),
                                FixCapability(
                                    id="c004",
                                    name="FixierenName",
                                    description="Fixieren Beschreibung",
                                    parameters=[
                                        Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 70]),
                                        Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 20]),
                                        PerfVolume(dimensionName="Fixiergeschwindigkeit", dimensionUnit="t/h", value=0.5)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                WorkerResourceAAS(
                    id="06b726ee3551415ca8e8aa749472b62f",
                    type="Worker",
                    name="Worker_002",
                    setups=[
                        Setup(
                            id="s004",
                            type="Qualification",
                            name="Schrauben",
                            capabilities=[
                                AdjustCapability(
                                    id="c003",
                                    name="JustierenName",
                                    description="Justieren Beschreibung",
                                    parameters=[
                                        PerfVolume(dimensionName="Justagegeschwindigkeit", dimensionUnit="t/h", value=1)
                                    ]
                                ),
                                AssemblyCapability(
                                    id="c004",
                                    name="FixierenName",
                                    description="Fixieren Beschreibung",
                                    parameters=[
                                       PerfVolume(dimensionName="Fixiergeschwindigkeit", dimensionUnit="t/h", value=0.5)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                WorkerResourceAAS(
                    id="dce9b3c20e6549e4a826c2a43da9ff9e",
                    type="Worker",
                    name="Worker_003",
                    setups=[
                        Setup(
                            id="s005",
                            type="Qualification",
                            name="Schrauben Anziehen",
                            capabilities=[
                                FixCapability(
                                    id="c004",
                                    name="FixierenName",
                                    description="Fixieren Beschreibung",
                                    parameters=[
                                        PerfVolume(dimensionName="Fixiergeschwindigkeit", dimensionUnit="t/h", value=0.5)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                WorkerResourceAAS(
                    id="2990c20b53f34f0391da3204a9824289",
                    type="Worker",
                    name="Worker_004",
                    setups=[
                        Setup(
                            id="s006",
                            type="Qualification",
                            name="Schrauben Anziehen",
                            capabilities=[
                                FixCapability(
                                    id="c004",
                                    name="FixierenName",
                                    description="Fixieren Beschreibung",
                                    parameters=[
                                       PerfVolume(dimensionName="Fixiergeschwindigkeit", dimensionUnit="t/h", value=1)
                                    ]
                                ),
                                ShakingCapability(
                                    id="c004",
                                    name="FixierenName",
                                    description="Fixieren Beschreibung",
                                    parameters=[
                                        PerfVolume(dimensionName="Fixiergeschwindigkeit", dimensionUnit="t/h", value=1)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                WorkerResourceAAS(
                    id="0850803e321e4b2d8eb4290bda18fa01",
                    type="Worker",
                    name="Worker_005",
                    setups=[
                        Setup(
                            id="s008",
                            type="Qualification",
                            name="Schrauben Anziehen",
                            capabilities=[
                                AssemblyCapability(
                                    id="c003",
                                    name="SchalenName",
                                    description="Schalen Beschreibung",
                                    parameters=[
                                        PerfVolume(dimensionName="Justagegeschwindigkeit", dimensionUnit="t/h",
                                                   value=0.5)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
TransportResourceAAS(
            id="3b6f1250ed5e47b6bd3d430c3158dd58",
            type="LKW",
            name="MAN 20t",
            setups=[
                Setup(
                id="s003",
                type="Transport",
                name="Hänger",
                    capabilities=[
                        TransportCapability(
                        id="c003",
                        name="Transport004",
                        description="Transport leichter Güter",
                        parameters=[
                            Weight(dimensionName="Traglast", dimensionUnit="t", valueRange=[0, 7]),
                            Velocity(dimensionName="Verfahrgeschwindigkeit", dimensionUnit="km/h", value=0.5),
                            PerfVolume(dimensionName="Verfahrvolumen", dimensionUnit="t/h", value=3),
                            Height(dimensionName="Verfahrhöhe", dimensionUnit="m", valueRange=[0, 15]),
                            Volume(dimensionName="Tragvolumen", dimensionUnit="m^3", valueRange=[0, 10])
                            ]
                        )
                    ]
                )
                ],
            ),
            ]
        )
    ]