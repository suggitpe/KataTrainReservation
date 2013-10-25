import urllib.request

url = "http://127.0.0.1:8082/booking_reference"

class BookingReferenceAccessor:
	def getBookingReference(self):
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req).read().decode("ISO-8859-1")
		#return "75bcd15"
		print(response)
		return str(response)
