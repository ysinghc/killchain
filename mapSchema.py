from dataclasses import dataclass
from typing import Optional

# --- Node Definitions ---

@dataclass
class Service:
    serviceId: str            # Unique service ID
    serviceName: str          # Human-readable name
    serviceType: str          # e.g., Web App, API, Database
    criticality: str          # Critical, High, Medium, Low
    exposureLevel: str        # Internal, DMZ, Public


@dataclass
class Asset:
    assetId: str              # Unique asset ID
    hostname: str             # Hostname of the machine/container
    ipAddress: str            # IP address
    assetType: str            # Server, Container, Network Device
    location: Optional[str]   # Physical or network location (optional)
    vulnerabilityScore: Optional[float]  # Vulnerability score (optional)


# --- Relationship Definitions ---

@dataclass
class DependsOn:
    dependencyType: str       # Data, API, Authentication, etc.
    criticality: str          # Local importance of this dependency
    dataFlow: str             # Unidirectional, Bidirectional


@dataclass
class CommunicatesWith:
    protocol: str             # HTTP, gRPC, etc.
    port: int
    frequency: str            # High, Medium, Low
    dataVolume: str           # Large, Medium, Small


@dataclass
class HostedOn:
    deploymentType: str       # Primary, Backup, DR


@dataclass
class ConnectsTo:
    networkSegment: str       # Segment or VLAN name
    connectionType: str       # Internal, VPN, Public
