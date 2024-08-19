QT += network

HEADERS += \
# Models
    $${PWD}/OAIFlux.h \
    $${PWD}/OAIFluxAtEnergy.h \
    $${PWD}/OAIFluxAtEnergy_flux.h \
    $${PWD}/OAIFlux_energies.h \
    $${PWD}/OAIFlux_flux.h \
# APIs
    $${PWD}/OAIGcrApi.h \
    $${PWD}/OAITrappedApi.h \
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
    $${PWD}/OAIFlux.cpp \
    $${PWD}/OAIFluxAtEnergy.cpp \
    $${PWD}/OAIFluxAtEnergy_flux.cpp \
    $${PWD}/OAIFlux_energies.cpp \
    $${PWD}/OAIFlux_flux.cpp \
# APIs
    $${PWD}/OAIGcrApi.cpp \
    $${PWD}/OAITrappedApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
