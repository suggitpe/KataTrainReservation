import unittest
from booking_ref_accessor import BookingReferenceAccessor

class BookingReferenceAccessorTest(unittest.TestCase):

	def test_callsOutToBookingRefServiceForAReference(self):
		accessor = BookingReferenceAccessor()
		bookingRef = accessor.getBookingReference()		
		assert len(bookingRef) > 4
		assert bookingRef[0:4] == '75bc' 


