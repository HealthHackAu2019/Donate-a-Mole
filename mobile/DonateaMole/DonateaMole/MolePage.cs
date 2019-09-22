using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Plugin.Permissions;
using Plugin.Permissions.Abstractions;

using Xamarin.Forms;

namespace DonateaMole
{
    public class MolePage : ContentPage
    {
        WebView webView = new WebView
        {
            VerticalOptions = LayoutOptions.FillAndExpand
        };

        public MolePage()
        {
            

            // Build the page.
            this.Content = new StackLayout
            {
                Children =
                {
                    //header,
                    webView
                }
            };

            //perms();
        }

        async void perms()
        {
            //var status = await CrossPermissions.Current.CheckPermissionStatusAsync(Permission.Camera);
            //if (status != PermissionStatus.Granted)
            //{
            //    if (await CrossPermissions.Current.ShouldShowRequestPermissionRationaleAsync(Permission.Camera))
            //    {
            //        await DisplayAlert("Need camera", "Gunna need that camera to take moles", "OK");
            //    }

            //    var results = await CrossPermissions.Current.RequestPermissionsAsync(Permission.Camera);
            //    status = results[Permission.Location];
            //}

            //if (status == PermissionStatus.Granted)
            //{
            //    webView.Source = new UrlWebViewSource
            //    {
            //        Url = "https://donateamole.org/",
            //    };
                
            //}
            //else if (status != PermissionStatus.Unknown)
            //{
            //    await DisplayAlert("Location Denied", "Can not continue, try again.", "OK");
            //}

        }
    }
}

