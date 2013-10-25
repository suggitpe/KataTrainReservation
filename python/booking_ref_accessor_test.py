import unittest
from booking_ref_accessor import BookingReferenceAccessor

class BookingReferenceAccessorTest(unittest.TestCase):

	def test_callsOutToBookingRefServiceForAReference(self):
		accessor = BookingReferenceAccessor()
		bookingRef = accessor.getBookingReference()		
		assert bookingRef == "75bcd15"


