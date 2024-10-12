QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssociatedRecord.h \
    $${PWD}/OAIBookingSchema.h \
    $${PWD}/OAICard.h \
    $${PWD}/OAIContact.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIHotelBookedResponse.h \
    $${PWD}/OAIHotelBookingLight.h \
    $${PWD}/OAIHotelBookingQuery.h \
    $${PWD}/OAIName.h \
    $${PWD}/OAIPayment.h \
    $${PWD}/OAIRoom.h \
    $${PWD}/OAIStakeholder.h \
    $${PWD}/OAIWarning.h \
# APIs
    $${PWD}/OAIBookingApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAssociatedRecord.cpp \
    $${PWD}/OAIBookingSchema.cpp \
    $${PWD}/OAICard.cpp \
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIHotelBookedResponse.cpp \
    $${PWD}/OAIHotelBookingLight.cpp \
    $${PWD}/OAIHotelBookingQuery.cpp \
    $${PWD}/OAIName.cpp \
    $${PWD}/OAIPayment.cpp \
    $${PWD}/OAIRoom.cpp \
    $${PWD}/OAIStakeholder.cpp \
    $${PWD}/OAIWarning.cpp \
# APIs
    $${PWD}/OAIBookingApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
