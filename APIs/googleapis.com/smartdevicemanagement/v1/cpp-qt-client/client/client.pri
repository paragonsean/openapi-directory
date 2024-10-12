QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1Device.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ListDevicesResponse.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ListRoomsResponse.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ListStructuresResponse.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ParentRelation.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1Room.h \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1Structure.h \
# APIs
    $${PWD}/OAIEnterprisesApi.h \
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
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1Device.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ListDevicesResponse.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ListRoomsResponse.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ListStructuresResponse.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1ParentRelation.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1Room.cpp \
    $${PWD}/OAIGoogleHomeEnterpriseSdmV1Structure.cpp \
# APIs
    $${PWD}/OAIEnterprisesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
