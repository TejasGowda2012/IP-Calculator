from django.shortcuts import render
import ipaddress

def home(request):
    result = None

    if request.method == "POST":
        ip = request.POST.get("ip")
        cidr = request.POST.get("cidr")

        network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)

        result = {
            "network": network.network_address,
            "broadcast": network.broadcast_address,
            "total": network.num_addresses,
            "usable": network.num_addresses - 2
        }

    return render(request, "calculator/index.html", {"result": result})
