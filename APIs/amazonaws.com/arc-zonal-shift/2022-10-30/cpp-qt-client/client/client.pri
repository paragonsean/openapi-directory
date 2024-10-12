QT += network

HEADERS += \
# Models
    $${PWD}/OAIAppliedStatus.h \
    $${PWD}/OAIGetManagedResourceResponse.h \
    $${PWD}/OAIListManagedResourcesResponse.h \
    $${PWD}/OAIListZonalShiftsResponse.h \
    $${PWD}/OAIManagedResourceSummary.h \
    $${PWD}/OAIStartZonalShiftRequest.h \
    $${PWD}/OAIStartZonalShift_request.h \
    $${PWD}/OAIUpdateZonalShiftRequest.h \
    $${PWD}/OAIUpdateZonalShift_request.h \
    $${PWD}/OAIZonalShift.h \
    $${PWD}/OAIZonalShiftInResource.h \
    $${PWD}/OAIZonalShiftStatus.h \
    $${PWD}/OAIZonalShiftSummary.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAppliedStatus.cpp \
    $${PWD}/OAIGetManagedResourceResponse.cpp \
    $${PWD}/OAIListManagedResourcesResponse.cpp \
    $${PWD}/OAIListZonalShiftsResponse.cpp \
    $${PWD}/OAIManagedResourceSummary.cpp \
    $${PWD}/OAIStartZonalShiftRequest.cpp \
    $${PWD}/OAIStartZonalShift_request.cpp \
    $${PWD}/OAIUpdateZonalShiftRequest.cpp \
    $${PWD}/OAIUpdateZonalShift_request.cpp \
    $${PWD}/OAIZonalShift.cpp \
    $${PWD}/OAIZonalShiftInResource.cpp \
    $${PWD}/OAIZonalShiftStatus.cpp \
    $${PWD}/OAIZonalShiftSummary.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
