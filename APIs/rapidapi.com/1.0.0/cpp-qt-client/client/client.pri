QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_first_quarter.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_first_quarter_current.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_first_quarter_next.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_full_moon.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_full_moon_current.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_full_moon_next.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_last_quarter.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_last_quarter_current.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_last_quarter_next.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_new_moon.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_new_moon_current.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_new_moon_next.h \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_sun.h \
    $${PWD}/OAIGetBasicMoonPhaseData_200_response.h \
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
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_first_quarter.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_first_quarter_current.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_first_quarter_next.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_full_moon.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_full_moon_current.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_full_moon_next.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_last_quarter.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_last_quarter_current.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_last_quarter_next.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_new_moon.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_new_moon_current.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_moon_phases_new_moon_next.cpp \
    $${PWD}/OAIGetAdvancedMoonPhaseData_200_response_sun.cpp \
    $${PWD}/OAIGetBasicMoonPhaseData_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
