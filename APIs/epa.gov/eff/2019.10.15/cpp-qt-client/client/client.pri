QT += network

HEADERS += \
# Models
    $${PWD}/OAIEff01.h \
    $${PWD}/OAIEff02.h \
    $${PWD}/OAIEff03.h \
    $${PWD}/OAIEff04.h \
    $${PWD}/OAIEff05.h \
    $${PWD}/OAIEff06.h \
    $${PWD}/OAIEff07.h \
    $${PWD}/OAIEff08.h \
    $${PWD}/OAIEff09.h \
    $${PWD}/OAIFormData_f_output.h \
    $${PWD}/OAIRlup01.h \
    $${PWD}/OAIRlup23.h \
    $${PWD}/OAI_eff_rest_services_get_effluent_chart_get_200_response.h \
    $${PWD}/OAI_eff_rest_services_get_summary_chart_get_200_response.h \
    $${PWD}/OAI_rest_lookups_cwa_parameters_get_200_response.h \
# APIs
    $${PWD}/OAIEffluentChartsApi.h \
    $${PWD}/OAILookupsApi.h \
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
    $${PWD}/OAIEff01.cpp \
    $${PWD}/OAIEff02.cpp \
    $${PWD}/OAIEff03.cpp \
    $${PWD}/OAIEff04.cpp \
    $${PWD}/OAIEff05.cpp \
    $${PWD}/OAIEff06.cpp \
    $${PWD}/OAIEff07.cpp \
    $${PWD}/OAIEff08.cpp \
    $${PWD}/OAIEff09.cpp \
    $${PWD}/OAIFormData_f_output.cpp \
    $${PWD}/OAIRlup01.cpp \
    $${PWD}/OAIRlup23.cpp \
    $${PWD}/OAI_eff_rest_services_get_effluent_chart_get_200_response.cpp \
    $${PWD}/OAI_eff_rest_services_get_summary_chart_get_200_response.cpp \
    $${PWD}/OAI_rest_lookups_cwa_parameters_get_200_response.cpp \
# APIs
    $${PWD}/OAIEffluentChartsApi.cpp \
    $${PWD}/OAILookupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
