<!DOCTYPE html>
<html>
<head>
    <title>IP Subnet Calculator</title>

    <style>
        body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: url("https://t4.ftcdn.net/jpg/17/15/62/53/360_F_1715625337_fqDCDcdIkymMTTk5lw1nZ4yCTKoIzEOi.jpg") no-repeat center center fixed;
    background-size: cover;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0;
}


        .box {
            width: 420px;
            background: #d7d5e4;
            padding: 25px 30px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 15px;
            outline: none;
            transition: border 0.3s;
        }

        input:focus {
            border-color: #667eea;
        }

        button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #667eea, #380071);
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.25);
        }

        hr {
            margin: 20px 0;
            border: none;
            border-top: 1px solid #ddd;
        }

        p {
            font-size: 15px;
            color: #444;
            margin: 8px 0;
        }

        p b {
            color: #222;
        }
    </style>
</head>

<body>

<div class="box">
    <h2>IP Address & Subnet Calculator</h2>

    <form method="POST">
        {% csrf_token %}
        <input type="text" name="ip" placeholder="Enter IP Address (192.168.1.10)" required>
        <input type="number" name="cidr" placeholder="Enter CIDR (24)" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result %}
    <hr>
    <p><b>Network ID:</b> {{ result.network }}</p>
    <p><b>Broadcast:</b> {{ result.broadcast }}</p>
    <p><b>Total Hosts:</b> {{ result.total }}</p>
    <p><b>Usable Hosts:</b> {{ result.usable }}</p>
    {% endif %}
</div>

</body>
</html>

