/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRouteFilter.h
 *
 * 
 */

#ifndef OAIRouteFilter_H
#define OAIRouteFilter_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRouteFilter : public OAIObject {
public:
    OAIRouteFilter();
    OAIRouteFilter(QString json);
    ~OAIRouteFilter() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDomainKey() const;
    void setDomainKey(const QString &domain_key);
    bool is_domain_key_Set() const;
    bool is_domain_key_Valid() const;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    QString getPathPrefix() const;
    void setPathPrefix(const QString &path_prefix);
    bool is_path_prefix_Set() const;
    bool is_path_prefix_Valid() const;

    QString getRouteKey() const;
    void setRouteKey(const QString &route_key);
    bool is_route_key_Set() const;
    bool is_route_key_Valid() const;

    QString getSharedRulesKey() const;
    void setSharedRulesKey(const QString &shared_rules_key);
    bool is_shared_rules_key_Set() const;
    bool is_shared_rules_key_Valid() const;

    QString getZoneKey() const;
    void setZoneKey(const QString &zone_key);
    bool is_zone_key_Set() const;
    bool is_zone_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_domain_key;
    bool m_domain_key_isSet;
    bool m_domain_key_isValid;

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    QString m_path_prefix;
    bool m_path_prefix_isSet;
    bool m_path_prefix_isValid;

    QString m_route_key;
    bool m_route_key_isSet;
    bool m_route_key_isValid;

    QString m_shared_rules_key;
    bool m_shared_rules_key_isSet;
    bool m_shared_rules_key_isValid;

    QString m_zone_key;
    bool m_zone_key_isSet;
    bool m_zone_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRouteFilter)

#endif // OAIRouteFilter_H
