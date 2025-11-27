<!-- Generieren Sie ein Mermaid-Diagramm vom Typ "flowchart", um entscheiden zu können, welchen Connector richtig ist -->

# Entscheidungslogik

1. **Erste Prüfung: OPC UA-Unterstützung**
   - Zunächst wird geprüft, ob die PLC das OPC UA-Protokoll unterstützt
   - Falls ja, wird der **OPC UA Connector** verwendet, da dies ein standardisiertes und modernes Kommunikationsprotokoll ist

2. **Zweite Prüfung: Siemens-PLC**
   - Wenn OPC UA nicht unterstützt wird, wird geprüft, ob es sich um eine Siemens-PLC handelt
   - Falls ja, wird der **S7 Connector** verwendet, der speziell für Siemens-Steuerungen entwickelt wurde

3. **Alternative: Ethernet/IP Connector**
   - Wenn weder OPC UA unterstützt wird noch eine Siemens-PLC vorliegt, wird der **Ethernet/IP Connector** als Standardlösung verwendet
