QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddClutter_request.h \
    $${PWD}/OAIAntenna.h \
    $${PWD}/OAIArea_request.h \
    $${PWD}/OAIEnvironment.h \
    $${PWD}/OAIFeature.h \
    $${PWD}/OAIModel.h \
    $${PWD}/OAIOutput.h \
    $${PWD}/OAIPath_request.h \
    $${PWD}/OAIPoint.h \
    $${PWD}/OAIPoints_request.h \
    $${PWD}/OAIReceiver.h \
    $${PWD}/OAITransmitter.h \
# APIs
    $${PWD}/OAIAnalyseApi.h \
    $${PWD}/OAICreateApi.h \
    $${PWD}/OAIManageApi.h \
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
    $${PWD}/OAIAddClutter_request.cpp \
    $${PWD}/OAIAntenna.cpp \
    $${PWD}/OAIArea_request.cpp \
    $${PWD}/OAIEnvironment.cpp \
    $${PWD}/OAIFeature.cpp \
    $${PWD}/OAIModel.cpp \
    $${PWD}/OAIOutput.cpp \
    $${PWD}/OAIPath_request.cpp \
    $${PWD}/OAIPoint.cpp \
    $${PWD}/OAIPoints_request.cpp \
    $${PWD}/OAIReceiver.cpp \
    $${PWD}/OAITransmitter.cpp \
# APIs
    $${PWD}/OAIAnalyseApi.cpp \
    $${PWD}/OAICreateApi.cpp \
    $${PWD}/OAIManageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
