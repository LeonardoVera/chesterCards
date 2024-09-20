from fasthtml.common import *

custom_css = Style("""
                .card-container {
                    display:flex;
                    flex-wrap:wrap;
                    height: 500px;
                    overflow-y: auto;
                    width: 100%;
                    background-color: #3a518c;
                }
                .card {
                    flex: 1 1 calc(33.333% - 10px);
                    margin: 5px;
                    box-sizing: border-box;
                    max-width: 350px;
                    min-width: 200px;
                }
                .main-container {
                    width: 100%;
                    display: flex;
                    height: 100vh;
                }
                .content {
                    width: 100%;
                    padding: 10px;
                    display: flex;
                    flex-direction: column;
                    height: 100%;
                }
                .header {
                    display: flex;
                    justify-content: space-between;
                    width: 100%;
                    padding: 10px;
                }
                .sidebar {
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    width: 500px;
                    padding: 10px;
                }
                .redes-sociales li{
                    text-decoration: none;
                    list-style: none;
                    display: inline;
                    margin-right: 10px;
                }
                .chester-profile{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                .chester-profile p{
                    margin: 0 10px;
                }
                .chester-profile h2{
                    margin: 15px 0px;
                    padding: 0;
                }
                .chester-profile img{
                    max-width: 60%;
                }
            """)