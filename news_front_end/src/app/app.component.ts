import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NewsArticleComponent } from './news-article/news-article.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,NewsArticleComponent,SearchBarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'news_front_end';
}
