QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddrecurrenceitemRequest.h \
    $${PWD}/OAIFrequency.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIReindexrecurrenceRequest.h \
    $${PWD}/OAIUpdatepartialrecurrenceRequest.h \
    $${PWD}/OAIUpdaterecurrenceRequest.h \
    $${PWD}/OAIUpdaterecurrencesettingsRequest.h \
# APIs
    $${PWD}/OAIMiscellaneousApi.h \
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
    $${PWD}/OAIAddrecurrenceitemRequest.cpp \
    $${PWD}/OAIFrequency.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIReindexrecurrenceRequest.cpp \
    $${PWD}/OAIUpdatepartialrecurrenceRequest.cpp \
    $${PWD}/OAIUpdaterecurrenceRequest.cpp \
    $${PWD}/OAIUpdaterecurrencesettingsRequest.cpp \
# APIs
    $${PWD}/OAIMiscellaneousApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
