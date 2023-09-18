messages = [
  {
    "id": "01A",
    "name": "Brake Operation Indicator",
    "period": 100,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Brake Operation Indicator",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "024",
    "name": "Brake Output Indicator",
    "period": 100,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Brake Output Indicator",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "146",
    "name": "Brake Oil Indicator",
    "period": 500,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Brake Oil Indicator",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "15A",
    "name": "Anti-lock Brake Operation",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Anti-lock Brake Operation",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "02F",
    "name": "Accelerator Pedal Operation Indicator",
    "period": 100,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Accelerator Pedal Operation Indicator",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "039",
    "name": "Throttle Position",
    "period": 100,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Throttle Position",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "16F",
    "name": "Throttle Adjustment",
    "period": 500,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Throttle Adjustment",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "043",
    "name": "Engine RPM. Speed",
    "period": 100,
    "DLC": 2,
    "pattern": r"(.{16})",
    "format": '################',
    "signals": [
        {
            "signal": "Engine RPM. Speed",
            "bitLength": 16,
            "bitStart": 0,
            "min": -32767,
            "max": 32766,
            "unit": "rpm",
            "scale": 1.00000,
            "offset": -32767
        }
    ]
  },
  {
    "id": "183",
    "name": "Engine Cooling Water Temperature",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{8})00000000",
    "format": '########00000000',
    "signals": [
        {
            "signal": "Engine Cooling Water Temperature",
            "bitLength": 8,
            "bitStart": 0,
            "min": -40,
            "max": 215,
            "unit": "C",
            "scale": 1.00000,
            "offset": -40
        }
    ]
  },
  {
    "id": "18D",
    "name": "Engine Malfunction",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Engine Malfunction",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "058",
    "name": "Steering Wheel Operation Position",
    "period": 100,
    "DLC": 2,
    "pattern": r"(.{16})",
    "format": '################',
    "signals": [
        {
            "signal": "Steering Wheel Operation Position",
            "bitLength": 16,
            "bitStart": 0,
            "min": -511,
            "max": 511,
            "unit": "%",
            "scale": 0.01559,
            "offset": -511
        }
    ]
  },
  {
    "id": "062",
    "name": "Power Steering Output Indicator",
    "period": 100,
    "DLC": 2,
    "pattern": r"000000(.{10})",
    "format": '000000##########',
    "signals": [
        {
            "signal": "Power Steering Output Indicator",
            "bitLength": 10,
            "bitStart": 6,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.09775,
            "offset": 0
        }
    ]
  },
  {
    "id": "198",
    "name": "Power Steering Malfunction",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Power Steering Malfunction",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "06D",
    "name": "Shift Position Switch",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Shift Position Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "1B8",
    "name": "Engine Start Button",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Engine Start Button",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "19A",
    "name": "Engine Status",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Engine Status",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "3D4",
    "name": "Fuel Amount",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{8})00000000",
    "format": '########00000000',
    "signals": [
        {
            "signal": "Fuel Amount",
            "bitLength": 8,
            "bitStart": 0,
            "min": 0,
            "max": 40,
            "unit": "Level",
            "scale": 0.15686,
            "offset": 0
        }
    ]
  },
  {
    "id": "3DE",
    "name": "Battery Warning",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Battery Warning",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "098",
    "name": "Horn Switch",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Horn Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "0A2",
    "name": "Horn Operation",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Horn Operation",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "1B1",
    "name": "Headlight Flashing Switch",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Headlight Flashing Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "271",
    "name": "Rear Wiper Switch",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Rear Wiper/Washer Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "27B",
    "name": "Rear Wiper Status",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Rear Wiper/Washer Status",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "286",
    "name": "Doors Lock/Unlock Switch",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Doors Lock/Unlock Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "1C9",
    "name": "Parking Brake",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Parking Brake",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "1D3",
    "name": "Parking Brake Status",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Parking Brake Status",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "29C",
    "name": "Right Door / Window Lifting Switch Position",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Right Door / Window Lifting Switch Position A / B",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "2B1",
    "name": "Left Door / Window Lifting Switch Position",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Lef Door / Window Lifting Switch Position A/B",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "0B4",
    "name": "Airbag Activation Switch",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Airbag Activation Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "457",
    "name": "Seat Belt Sensor",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Seat Belt Sensor",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "461",
    "name": "Seat Belt Alarm",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Seat Belt Alarm",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "46C",
    "name": "Bonnet(Hood) Open/Close Switch",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Bonnet(Hood) Open/Close Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "477",
    "name": "Trunk Open/Close Switch",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Trunk Open/Close Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "482",
    "name": "Eco-driving Judgment",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{1})000000000000000",
    "format": '#000000000000000',
    "signals": [
        {
            "signal": "Eco-driving Judgment",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "077",
    "name": "Shift Position",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})(.{1})(.{1})(.{1})00000000000",
    "format": '#####00000000000',
    "signals": [
        {
            "signal": "Shift Position A",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Shift Position B",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Shift Position C",
            "bitLength": 1,
            "bitStart": 2,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Shift Position D",
            "bitLength": 1,
            "bitStart": 3,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Shift Position E",
            "bitLength": 1,
            "bitStart": 4,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "083",
    "name": "Right/Left Turn Signal, Hazard Switch",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})(.{1})0000000000000",
    "format": '###0000000000000',
    "signals": [
        {
            "signal": "Right Turn Signal",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Left Turn Signal",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Hazard Switch",
            "bitLength": 1,
            "bitStart": 2,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "08D",
    "name": "Turn Signal Indicator",
    "period": 100,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})(.{1})0000000000000",
    "format": '###0000000000000',
    "signals": [
        {
            "signal": "Turn Signal Indicator Status A",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Turn Signal Indicator Status B",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Turn Signal Indicator Status C",
            "bitLength": 1,
            "bitStart": 2,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "1A7",
    "name": "Head Lights/Beam Switch",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})00000000000000",
    "format": '##00000000000000',
    "signals": [
        {
            "signal": "Head Lights Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "High Beam Switch",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "1BB",
    "name": "Head Lights/Beam Indicator",
    "period": 500,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})00000000000000",
    "format": '##00000000000000',
    "signals": [
        {
            "signal": "Head Lights Indicator",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "High Beam Indicator",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "25C",
    "name": "Front Wiper Switch",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})(.{1})(.{1})000000000000",
    "format": '####000000000000',
    "signals": [
        {
            "signal": "Front Wiper Intermittent Switch",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Front Wiper LOW Switch",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Front Wiper HIGH Switch",
            "bitLength": 1,
            "bitStart": 2,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Front Wiper Washer Switch",
            "bitLength": 1,
            "bitStart": 3,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "266",
    "name": "Front Wiper Status",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})(.{1})(.{1})000000000000",
    "format": '####000000000000',
    "signals": [
        {
            "signal": "Front Wiper Intermittent Status",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Front Wiper LOW Status",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Front Wiper HIGH Status",
            "bitLength": 1,
            "bitStart": 2,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Front Wiper Washer Status",
            "bitLength": 1,
            "bitStart": 3,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "420",
    "name": "Door Lock Drive Unit Malfunction",
    "period": 5000,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})(.{1})0000000000000",
    "format": '###0000000000000',
    "signals": [
        {
            "signal": "Door Lock Drive Unit Malfunction Status A",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Door Lock Drive Unit Malfunction Status B",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Door Lock Drive Unit Malfunction Status C",
            "bitLength": 1,
            "bitStart": 2,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "290",
    "name": "Doors Open/Close | Locked/Unlocked Indicator",
    "period": 1000,
    "DLC": 1,
    "pattern": r"(.{1})(.{1})00000000000000",
    "format": '##00000000000000',
    "signals": [
        {
            "signal": "Doors Open/Close Indicator",
            "bitLength": 1,
            "bitStart": 0,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        },
        {
            "signal": "Doors Locked/Unlocked Indicator",
            "bitLength": 1,
            "bitStart": 1,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
    ]
  },
  {
    "id": "2A6",
    "name": "Right Door Window Position, Limit Switch",
    "period": 1000,
    "DLC": 2,
    "pattern": r"(.{8})0000000(.{1})",
    "format": '########0000000#',
    "signals": [
        {
            "signal": "Limit Switch Status",
            "bitLength": 8,
            "bitStart": 0,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.39216,
            "offset": 0
        },
        {
            "signal": "Right Door / Window Position A / B",
            "bitLength": 1,
            "bitStart": 15,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }        
    ]
  },
  {
    "id": "2BB",
    "name": "Left Door Window Position, Limit Switch",
    "period": 1000,
    "DLC": 2,
    "pattern": r"(.{8})0000000(.{1})",
    "format": '########0000000#',
    "signals": [
        {
            "signal": "Limit Switch Status",
            "bitLength": 8,
            "bitStart": 0,
            "min": 0,
            "max": 100,
            "unit": "%",
            "scale": 0.39216,
            "offset": 0
        },
        {
            "signal": "Left Door / Window Position A / B",
            "bitLength": 1,
            "bitStart": 15,
            "min": 0,
            "max": 1,
            "unit": "ON/OFF",
            "scale": 1.00000,
            "offset": 0
        }
        
    ]
  },
]