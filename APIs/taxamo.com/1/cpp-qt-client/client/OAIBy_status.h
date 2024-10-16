/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBy_status.h
 *
 * 
 */

#ifndef OAIBy_status_H
#define OAIBy_status_H

#include <QJsonObject>

#include "OAIC.h"
#include "OAIN.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIC;
class OAIN;

class OAIBy_status : public OAIObject {
public:
    OAIBy_status();
    OAIBy_status(QString json);
    ~OAIBy_status() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIC> getC() const;
    void setC(const QList<OAIC> &c);
    bool is_c_Set() const;
    bool is_c_Valid() const;

    QList<OAIN> getN() const;
    void setN(const QList<OAIN> &n);
    bool is_n_Set() const;
    bool is_n_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIC> m_c;
    bool m_c_isSet;
    bool m_c_isValid;

    QList<OAIN> m_n;
    bool m_n_isSet;
    bool m_n_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBy_status)

#endif // OAIBy_status_H
