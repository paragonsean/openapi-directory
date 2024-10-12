QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutocompleteSearchSuggestions.h \
    $${PWD}/OAIAutocompleteSearchSuggestions_searches_inner.h \
    $${PWD}/OAIAutocompleteSearchSuggestions_searches_inner_attributes_inner.h \
    $${PWD}/OAIBanners.h \
    $${PWD}/OAIBanners_banners_inner.h \
    $${PWD}/OAICorrection.h \
    $${PWD}/OAICorrection_correction.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIFacets.h \
    $${PWD}/OAIFacets_breadcrumb_inner.h \
    $${PWD}/OAIFacets_facets_inner.h \
    $${PWD}/OAIFacets_facets_inner_values_inner.h \
    $${PWD}/OAIFacets_queryArgs.h \
    $${PWD}/OAIFacets_queryArgs_selectedFacets_inner.h \
    $${PWD}/OAIProductSearch.h \
    $${PWD}/OAIProductSearch_correction.h \
    $${PWD}/OAISearchSuggestions.h \
    $${PWD}/OAISearchSuggestions_searches_inner.h \
    $${PWD}/OAITopSearches.h \
# APIs
    $${PWD}/OAIAutocompleteApi.h \
    $${PWD}/OAIProductListPageApi.h \
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
    $${PWD}/OAIAutocompleteSearchSuggestions.cpp \
    $${PWD}/OAIAutocompleteSearchSuggestions_searches_inner.cpp \
    $${PWD}/OAIAutocompleteSearchSuggestions_searches_inner_attributes_inner.cpp \
    $${PWD}/OAIBanners.cpp \
    $${PWD}/OAIBanners_banners_inner.cpp \
    $${PWD}/OAICorrection.cpp \
    $${PWD}/OAICorrection_correction.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIFacets.cpp \
    $${PWD}/OAIFacets_breadcrumb_inner.cpp \
    $${PWD}/OAIFacets_facets_inner.cpp \
    $${PWD}/OAIFacets_facets_inner_values_inner.cpp \
    $${PWD}/OAIFacets_queryArgs.cpp \
    $${PWD}/OAIFacets_queryArgs_selectedFacets_inner.cpp \
    $${PWD}/OAIProductSearch.cpp \
    $${PWD}/OAIProductSearch_correction.cpp \
    $${PWD}/OAISearchSuggestions.cpp \
    $${PWD}/OAISearchSuggestions_searches_inner.cpp \
    $${PWD}/OAITopSearches.cpp \
# APIs
    $${PWD}/OAIAutocompleteApi.cpp \
    $${PWD}/OAIProductListPageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
