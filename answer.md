# Task 12 – Re-evaluate and Adapt the Design

## A. Impact analysis
The new requirement adds a private 5G network and 50 AGVs. Retain the fibre backbone and wired fixed-device network, but modify wireless access and traffic separation:
- 5G URLLC for AGV command/control, subject to coverage and latency validation.
- URLLC/industrial wired Ethernet for robot control.
- Wi-Fi 6 for office users.
- Fibre for backbone and data-centre connections.

The assignment does not specify AGV message size or reporting interval, so an exact AGV Mbps total cannot be calculated without an assumption. Use:
`AGV traffic (Mbps) = 50 × message_bytes × 8 / interval_seconds / 1,000,000`.
Record the chosen measured or specified values before final submission.

## B. Test original design
Original Wi-Fi handover is approximately 150 ms, which is 15 times the 10 ms command deadline. Private 5G handover is approximately 20 ms, still twice the deadline. Therefore neither stated handover interruption alone guarantees the 10 ms requirement. Test make-before-break/dual connectivity, redundant coverage, local control autonomy and actual end-to-end latency.

For the 1.2 km route at 2 m/s, travel time is 600 s. Approximate transitions: 39 Wi-Fi handovers (5.85 s total interruption) versus 3 5G handovers (60 ms total interruption).

## C. Adaptation
**Decision: MODIFY the original design.**
- Keep fibre backbone and wired robot cells.
- Deploy private 5G for 50 AGVs with overlapping cells and validated mobility.
- Use URLLC QoS/slicing where supported.
- Keep office users on Wi-Fi 6.
- Keep CCTV on wired Ethernet with local recording.
- Separate traffic with VLANs, QoS and firewall policies.

## D. Evidence-based defence
The original 8-line peak load is 1.26592 Gbps, exceeding a 1 Gbps uplink. Motion-triggered CCTV reduces the calculated eight-line load to 536.32 Mbps. The stated Wi-Fi and 5G handover times (150 ms and 20 ms) both exceed the 10 ms command deadline. Therefore the best choice is a modified hybrid network, not an all-wireless redesign. Capture actual AGV traffic, handover and latency tests before claiming the design meets the deadline.
