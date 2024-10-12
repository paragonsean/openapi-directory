QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvertisedId.h \
    $${PWD}/OAIAttachmentInfo.h \
    $${PWD}/OAIBeacon.h \
    $${PWD}/OAIBeaconAttachment.h \
    $${PWD}/OAIBeaconInfo.h \
    $${PWD}/OAIDate.h \
    $${PWD}/OAIDeleteAttachmentsResponse.h \
    $${PWD}/OAIDiagnostics.h \
    $${PWD}/OAIEphemeralIdRegistration.h \
    $${PWD}/OAIEphemeralIdRegistrationParams.h \
    $${PWD}/OAIGetInfoForObservedBeaconsRequest.h \
    $${PWD}/OAIGetInfoForObservedBeaconsResponse.h \
    $${PWD}/OAIIndoorLevel.h \
    $${PWD}/OAILatLng.h \
    $${PWD}/OAIListBeaconAttachmentsResponse.h \
    $${PWD}/OAIListBeaconsResponse.h \
    $${PWD}/OAIListDiagnosticsResponse.h \
    $${PWD}/OAIListNamespacesResponse.h \
    $${PWD}/OAINamespace.h \
    $${PWD}/OAIObservation.h \
# APIs
    $${PWD}/OAIBeaconinfoApi.h \
    $${PWD}/OAIBeaconsApi.h \
    $${PWD}/OAINamespacesApi.h \
    $${PWD}/OAIV1beta1Api.h \
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
    $${PWD}/OAIAdvertisedId.cpp \
    $${PWD}/OAIAttachmentInfo.cpp \
    $${PWD}/OAIBeacon.cpp \
    $${PWD}/OAIBeaconAttachment.cpp \
    $${PWD}/OAIBeaconInfo.cpp \
    $${PWD}/OAIDate.cpp \
    $${PWD}/OAIDeleteAttachmentsResponse.cpp \
    $${PWD}/OAIDiagnostics.cpp \
    $${PWD}/OAIEphemeralIdRegistration.cpp \
    $${PWD}/OAIEphemeralIdRegistrationParams.cpp \
    $${PWD}/OAIGetInfoForObservedBeaconsRequest.cpp \
    $${PWD}/OAIGetInfoForObservedBeaconsResponse.cpp \
    $${PWD}/OAIIndoorLevel.cpp \
    $${PWD}/OAILatLng.cpp \
    $${PWD}/OAIListBeaconAttachmentsResponse.cpp \
    $${PWD}/OAIListBeaconsResponse.cpp \
    $${PWD}/OAIListDiagnosticsResponse.cpp \
    $${PWD}/OAIListNamespacesResponse.cpp \
    $${PWD}/OAINamespace.cpp \
    $${PWD}/OAIObservation.cpp \
# APIs
    $${PWD}/OAIBeaconinfoApi.cpp \
    $${PWD}/OAIBeaconsApi.cpp \
    $${PWD}/OAINamespacesApi.cpp \
    $${PWD}/OAIV1beta1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
