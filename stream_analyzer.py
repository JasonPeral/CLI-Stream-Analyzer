import subprocess

def menu():
	print("Welcome to MCast Stream analyzer")
	print("1. Check stream bitrate")
	print("2. check codec and stream info)
	print("3. run full error check")
	print("4. Analyze audio levels)
	print("5. Exit")


def get_mcast():
	return input ("Enter the multicast you want to analyze(with port)")


while True:
	menu()
	choice = input("\n Choose analyzing option from above").strip()

	if choice == "5":
		print("Exiting..")
		break

	url = get_mcast()

