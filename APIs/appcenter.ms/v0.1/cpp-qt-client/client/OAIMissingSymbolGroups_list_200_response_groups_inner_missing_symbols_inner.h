/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner.h
 *
 * missing symbol
 */

#ifndef OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner_H
#define OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner : public OAIObject {
public:
    OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner();
    OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner(QString json);
    ~OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPlatform() const;
    void setPlatform(const QString &platform);
    bool is_platform_Set() const;
    bool is_platform_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getSymbolId() const;
    void setSymbolId(const QString &symbol_id);
    bool is_symbol_id_Set() const;
    bool is_symbol_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_platform;
    bool m_platform_isSet;
    bool m_platform_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_symbol_id;
    bool m_symbol_id_isSet;
    bool m_symbol_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner)

#endif // OAIMissingSymbolGroups_list_200_response_groups_inner_missing_symbols_inner_H
