import pigpio
import time


def main():
    # Definitions
    pin_status: int = 17
    pin_control: int = 18
    wait_sec: int = 5 * 60
    run_cycle_sec: int = 1

    pi = pigpio.pi()
    # Configure pins
    pi.set_mode(pin_status, pigpio.INPUT)
    pi.set_pull_up_down(pin_status, pigpio.PUD_UP)
    pi.set_mode(pin_control, pigpio.OUTPUT)
    pi.set_pull_up_down(pin_control, pigpio.PUD_DOWN)
    pi.write(pin_control, 1)

    while True:
        # Read status
        status = pi.read(pin_status)

        if status == 1:
            pi.write(pin_control, 1)
        elif status == 0:
            # Wait and check if the status is still 0 afterwards.
            time.sleep(wait_sec)
            status = pi.read(pin_status)

            if status == 0:
                pi.write(pin_control, 0)

        # Save CPU
        time.sleep(run_cycle_sec)


if __name__ == "__main__":  # pragma: no cover
    main()
