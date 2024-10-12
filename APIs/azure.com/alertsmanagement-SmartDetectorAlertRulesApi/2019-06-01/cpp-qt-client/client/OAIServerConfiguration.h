/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Representing a Server configuration.
 */
#ifndef OAI_SERVERVCONFIGURATION_H
#define OAI_SERVERVCONFIGURATION_H

#include <QString>
#include <QMap>
#include <QRegularExpression>
#include <QUrl>
#include <stdexcept>
#include "OAIServerVariable.h"

namespace OpenAPI {

class OAIServerConfiguration {
public:
    /**
     * @param url A URL to the target host.
     * @param description A description of the host designated by the URL.
     * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
     */
    OAIServerConfiguration(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables)
    : _description(description),
      _variables(variables),
      _url(url){}
    OAIServerConfiguration(){}
    ~OAIServerConfiguration(){}

    /**
     * Format URL template using given variables.
     *
     * @param variables A map between a variable name and its value.
     * @return Formatted URL.
     */
    QString URL() {
        QString url = _url.toString();
        if(!_variables.empty()){
            // go through variables and replace placeholders
            for (auto const& v : _variables.keys()) {
                QString name = v;
                OAIServerVariable serverVariable = _variables.value(v);
                QString value = serverVariable._defaultValue;

                if (!serverVariable._enumValues.empty() && !serverVariable._enumValues.contains(value)) {
                    throw std::runtime_error(QString("The variable " + name + " in the server URL has invalid value " + value + ".").toUtf8().toStdString());
                }
                QRegularExpression regex(QString("\\{" + name + "\\}"));
                url = url.replace(regex, value);

            }
            return url;
        }
        return url;
    }

    int setDefaultValue(const QString &variable,const QString &value){
      if(_variables.contains(variable))
        return _variables[variable].setDefaultValue(value);
      return -1;
    }

    QString _description;
    QMap<QString, OAIServerVariable> _variables;
    QUrl _url;

};

} // namespace OpenAPI

#endif // OAI_SERVERVCONFIGURATION_H
