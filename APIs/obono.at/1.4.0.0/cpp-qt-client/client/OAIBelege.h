/**
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBelege.h
 *
 * 
 */

#ifndef OAIBelege_H
#define OAIBelege_H

#include <QJsonObject>

#include "OAIBeleg.h"
#include "OAIExportformat_Belege_Gruppe_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBeleg;
class OAIExportformat_Belege_Gruppe_inner;

class OAIBelege : public OAIObject {
public:
    OAIBelege();
    OAIBelege(QString json);
    ~OAIBelege() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIBeleg> getBelege() const;
    void setBelege(const QList<OAIBeleg> &belege);
    bool is_belege_Set() const;
    bool is_belege_Valid() const;

    QList<OAIExportformat_Belege_Gruppe_inner> getBelegeGruppe() const;
    void setBelegeGruppe(const QList<OAIExportformat_Belege_Gruppe_inner> &belege_gruppe);
    bool is_belege_gruppe_Set() const;
    bool is_belege_gruppe_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIBeleg> m_belege;
    bool m_belege_isSet;
    bool m_belege_isValid;

    QList<OAIExportformat_Belege_Gruppe_inner> m_belege_gruppe;
    bool m_belege_gruppe_isSet;
    bool m_belege_gruppe_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBelege)

#endif // OAIBelege_H
